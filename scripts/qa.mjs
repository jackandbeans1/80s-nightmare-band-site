import crypto from "node:crypto";
import fs from "node:fs";
import path from "node:path";

const root = process.cwd();
const publicDir = path.join(root, "public");
const approvedDir = path.join(root, "source-assets", "brand", "anos-r2.1");
const failures = [];

function fail(message) {
  failures.push(message);
}

function walk(directory) {
  return fs.readdirSync(directory, { withFileTypes: true }).flatMap((entry) => {
    const target = path.join(directory, entry.name);
    return entry.isDirectory() ? walk(target) : [target];
  });
}

function sha256(file) {
  return crypto.createHash("sha256").update(fs.readFileSync(file)).digest("hex");
}

function assertExactCopy(publicRelative, sourceRelative) {
  const publicFile = path.join(publicDir, publicRelative);
  const sourceFile = path.join(approvedDir, sourceRelative);
  if (!fs.existsSync(publicFile) || !fs.existsSync(sourceFile)) {
    fail(`Missing approved asset pair: ${publicRelative} / ${sourceRelative}`);
    return;
  }
  if (sha256(publicFile) !== sha256(sourceFile)) {
    fail(`Public asset differs from approved master: ${publicRelative}`);
  }
}

function resolvePublicReference(reference) {
  const clean = reference.split(/[?#]/, 1)[0];
  if (!clean.startsWith("/") || clean === "/") {
    return clean === "/" ? path.join(publicDir, "index.html") : null;
  }
  const candidate = path.join(publicDir, clean.slice(1));
  if (clean.endsWith("/")) return path.join(candidate, "index.html");
  return candidate;
}

function readPngSize(file) {
  const data = fs.readFileSync(file);
  const signature = "89504e470d0a1a0a";
  if (data.subarray(0, 8).toString("hex") !== signature) {
    fail(`Invalid PNG signature: ${path.relative(root, file)}`);
    return null;
  }
  return [data.readUInt32BE(16), data.readUInt32BE(20)];
}

assertExactCopy("assets/logo.svg", "03_PRIMARY_YELLOW/anos-primary-yellow-r2.svg");
assertExactCopy("assets/logo-digital-magenta.svg", "04_DIGITAL_MAGENTA/anos-digital-magenta-r2.svg");
assertExactCopy("assets/logo-onecolor-light.svg", "05_ONE_COLOR/anos-onecolor-light-r2.svg");
assertExactCopy("assets/mark-80s.svg", "06_SMALL_SIZE_AND_SOCIAL/anos-micro-80s-yellow-r2.svg");
assertExactCopy("assets/social-80s-black.svg", "06_SMALL_SIZE_AND_SOCIAL/anos-social-icon-black-r2.svg");
assertExactCopy("assets/social-80s-transparent.svg", "06_SMALL_SIZE_AND_SOCIAL/anos-social-icon-transparent-r2.svg");
assertExactCopy("assets/social-80s-1024.png", "06_SMALL_SIZE_AND_SOCIAL/anos-social-1024-r2.png");
assertExactCopy("assets/favicon.svg", "06_SMALL_SIZE_AND_SOCIAL/anos-favicon-master-32-r2.svg");
assertExactCopy("assets/favicon-16.png", "06_SMALL_SIZE_AND_SOCIAL/anos-favicon-16-r2.png");
assertExactCopy("assets/favicon-32.png", "06_SMALL_SIZE_AND_SOCIAL/anos-favicon-32-r2.png");
assertExactCopy("assets/favicon-48.png", "06_SMALL_SIZE_AND_SOCIAL/anos-favicon-48-r2.png");

const approvedWebSvgs = [
  "logo.svg",
  "logo-digital-magenta.svg",
  "logo-onecolor-light.svg",
  "mark-80s.svg",
  "social-80s-black.svg",
  "social-80s-transparent.svg",
  "favicon.svg",
];
for (const name of approvedWebSvgs) {
  const text = fs.readFileSync(path.join(publicDir, "assets", name), "utf8");
  if (/<(?:text|image|filter|mask|clipPath|linearGradient|radialGradient)\b/i.test(text)) {
    fail(`Unsupported SVG construct in approved web asset: ${name}`);
  }
}

const expectedPngSizes = new Map([
  ["favicon-16.png", [16, 16]],
  ["favicon-32.png", [32, 32]],
  ["favicon-48.png", [48, 48]],
  ["apple-touch-icon.png", [180, 180]],
  ["icon-192.png", [192, 192]],
  ["icon-512.png", [512, 512]],
  ["social-80s-1024.png", [1024, 1024]],
]);
for (const [name, expected] of expectedPngSizes) {
  const file = path.join(publicDir, "assets", name);
  if (!fs.existsSync(file)) {
    fail(`Missing platform image: ${name}`);
    continue;
  }
  const actual = readPngSize(file);
  if (actual && (actual[0] !== expected[0] || actual[1] !== expected[1])) {
    fail(`Incorrect dimensions for ${name}: ${actual.join("x")}`);
  }
}

const ico = fs.readFileSync(path.join(publicDir, "favicon.ico"));
if (ico.length < 6 || ico.readUInt16LE(0) !== 0 || ico.readUInt16LE(2) !== 1 || ico.readUInt16LE(4) !== 3) {
  fail("favicon.ico is not a valid three-image icon container");
}

const mojibake = [
  "\u00e2\u20ac\u2122",
  "\u00e2\u20ac\u201d",
  "\u00e2\u20ac\u201c",
  "\u00e2\u2020",
  "\u00c2\u00a9",
  "\u00c2\u00b7",
  "\u00e2\u20ac\u00a6",
  "\ufffd",
];
const textFiles = walk(publicDir).filter((file) =>
  [".html", ".css", ".js", ".json", ".xml", ".svg", ".webmanifest", ""].includes(path.extname(file).toLowerCase()),
);
for (const file of textFiles) {
  const text = fs.readFileSync(file, "utf8");
  if (mojibake.some((marker) => text.includes(marker))) {
    fail(`Encoding-corruption marker found: ${path.relative(root, file)}`);
  }
}

const deprecatedReference = /logo-(?:blood-moon|midnight-signal|aftershock-yellow|badge|nightmare-fuel)|logo\.png\b/i;
const htmlFiles = walk(publicDir).filter((file) => file.endsWith(".html"));
for (const file of htmlFiles) {
  const html = fs.readFileSync(file, "utf8");
  if (deprecatedReference.test(html)) {
    fail(`Deprecated logo reference remains in ${path.relative(root, file)}`);
  }
  for (const required of [
    "/favicon.ico?v=20260814",
    "/assets/favicon-16.png?v=20260814",
    "/assets/favicon-32.png?v=20260814",
    "/assets/favicon.svg?v=20260814",
    "/assets/apple-touch-icon.png?v=20260814",
    "/site.webmanifest?v=20260814",
  ]) {
    if (!html.includes(required)) fail(`Missing ${required} in ${path.relative(root, file)}`);
  }
  for (const match of html.matchAll(/<(?:img|script|link|a)\b[^>]*(?:src|href)="([^"]+)"[^>]*>/gi)) {
    const reference = match[1];
    if (/^(?:https?:|mailto:|tel:|#|javascript:)/i.test(reference)) continue;
    const target = resolvePublicReference(reference);
    if (target && !fs.existsSync(target)) {
      fail(`Broken local reference in ${path.relative(root, file)}: ${reference}`);
    }
  }
  for (const match of html.matchAll(/<script\s+type="application\/ld\+json">([\s\S]*?)<\/script>/gi)) {
    try {
      JSON.parse(match[1]);
    } catch (error) {
      fail(`Invalid JSON-LD in ${path.relative(root, file)}: ${error.message}`);
    }
  }
}

let manifest;
try {
  manifest = JSON.parse(fs.readFileSync(path.join(publicDir, "site.webmanifest"), "utf8"));
} catch (error) {
  fail(`Invalid site.webmanifest: ${error.message}`);
}
if (manifest) {
  for (const icon of manifest.icons ?? []) {
    const target = resolvePublicReference(icon.src);
    if (!target || !fs.existsSync(target)) fail(`Missing manifest icon: ${icon.src}`);
  }
  if ((manifest.icons ?? []).some((icon) => icon.purpose?.includes("maskable"))) {
    fail("Maskable icon declared without a separately validated maskable-safe asset");
  }
}

if (failures.length) {
  console.error(`QA failed with ${failures.length} issue(s):`);
  for (const failure of failures) console.error(`- ${failure}`);
  process.exit(1);
}

console.log(`QA passed: ${htmlFiles.length} HTML pages, approved asset integrity, platform icons, local references, JSON-LD, manifest, and encoding checks.`);
