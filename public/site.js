const header = document.querySelector("[data-header]");
const menuButton = document.querySelector("[data-menu-toggle]");
const nav = document.querySelector("[data-nav]");

const closeMenu = () => {
  menuButton?.setAttribute("aria-expanded", "false");
  nav?.classList.remove("open");
  document.body.classList.remove("menu-open");
};

menuButton?.addEventListener("click", () => {
  const open = menuButton.getAttribute("aria-expanded") === "true";
  menuButton.setAttribute("aria-expanded", String(!open));
  nav?.classList.toggle("open", !open);
  document.body.classList.toggle("menu-open", !open);
});

nav?.querySelectorAll("a").forEach((link) => link.addEventListener("click", closeMenu));
window.addEventListener("keydown", (event) => {
  if (event.key === "Escape") closeMenu();
});

const updateHeader = () => header?.classList.toggle("scrolled", window.scrollY > 16);
updateHeader();
window.addEventListener("scroll", updateHeader, { passive: true });

const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("is-visible");
        observer.unobserve(entry.target);
      }
    });
  },
  { rootMargin: "0px 0px -8%", threshold: 0.08 }
);

document.querySelectorAll(".reveal").forEach((element) => observer.observe(element));
document.querySelector("[data-year]").textContent = String(new Date().getFullYear());

document.querySelector("[data-booking-form]")?.addEventListener("submit", (event) => {
  event.preventDefault();
  const form = event.currentTarget;
  if (!form.reportValidity()) return;

  const data = new FormData(form);
  const venue = String(data.get("venue") || "").trim();
  const date = String(data.get("date") || "Not set").trim();
  const email = String(data.get("email") || "").trim();
  const details = String(data.get("details") || "").trim();
  const subject = `Booking enquiry — ${venue}`;
  const body = [
    "Hello A Nightmare on 80s Street,",
    "",
    `Venue / organization: ${venue}`,
    `Event date: ${date}`,
    `Contact email: ${email}`,
    "",
    "Event details:",
    details,
    "",
    "Thanks!"
  ].join("\n");

  window.location.href = `mailto:80snightmareband@gmail.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
});
