"use strict";

const menuToggle = document.querySelector(".menu-toggle");
const primaryNav = document.querySelector(".primary-nav");

if (menuToggle && primaryNav) {
  const closeMenu = () => {
    menuToggle.setAttribute("aria-expanded", "false");
    menuToggle.setAttribute("aria-label", "Open navigation menu");
    primaryNav.classList.remove("is-open");
  };

  menuToggle.addEventListener("click", () => {
    const isOpen = menuToggle.getAttribute("aria-expanded") === "true";
    menuToggle.setAttribute("aria-expanded", String(!isOpen));
    menuToggle.setAttribute("aria-label", isOpen ? "Open navigation menu" : "Close navigation menu");
    primaryNav.classList.toggle("is-open", !isOpen);
  });

  primaryNav.querySelectorAll("a").forEach((link) => link.addEventListener("click", closeMenu));
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") closeMenu();
  });
  window.addEventListener("resize", () => {
    if (window.innerWidth > 820) closeMenu();
  });
}

const curriculumToggles = document.querySelectorAll(".curriculum-toggle");
curriculumToggles.forEach((toggle) => {
  toggle.addEventListener("click", () => {
    const wasExpanded = toggle.getAttribute("aria-expanded") === "true";
    curriculumToggles.forEach((otherToggle) => {
      otherToggle.setAttribute("aria-expanded", "false");
      const otherPanel = document.getElementById(otherToggle.getAttribute("aria-controls"));
      const otherGroup = otherToggle.closest(".curriculum-group");
      if (otherPanel) otherPanel.hidden = true;
      if (otherGroup) otherGroup.classList.remove("is-open");
    });

    if (!wasExpanded) {
      toggle.setAttribute("aria-expanded", "true");
      const panel = document.getElementById(toggle.getAttribute("aria-controls"));
      const group = toggle.closest(".curriculum-group");
      if (panel) panel.hidden = false;
      if (group) group.classList.add("is-open");
    }
  });
});

const scenarios = {
  mfa: {
    question: "“I can’t set up my MFA device. What should I do?”",
    status: "ANSWER WITH EVIDENCE",
    statusClass: "status-answered",
    icon: "✓",
    iconClass: "",
    answer: "“I can help. Follow the approved MFA setup guide. If you’re locked out, contact Identity Support through the company directory.”",
    source: "it.mfa.01",
    sourceNote: "· current approved source",
    trace: ["authenticate", "retrieve", "cite source"],
  },
  admin: {
    question: "“Can you grant me admin access before my shift?”",
    status: "HUMAN REVIEW REQUIRED",
    statusClass: "status-escalate",
    icon: "↗",
    iconClass: "icon-escalate",
    answer: "“I can’t grant privileged access in chat. I’ll route your request to an authorized owner to review.”",
    source: "authorized_support_owner",
    sourceNote: "· approval boundary",
    trace: ["authenticate", "policy check", "human handoff"],
  },
  unknown: {
    question: "“What’s on the cafeteria menu this Friday?”",
    status: "ASK / HAND OFF",
    statusClass: "status-clarify",
    icon: "?",
    iconClass: "icon-clarify",
    answer: "“I couldn’t find an approved, current guide for that. Is there a location or café you mean? I can route this to the support team.”",
    source: "No source returned",
    sourceNote: "· safe clarification",
    trace: ["authenticate", "search approved sources", "clarify"],
  },
};

const scenarioButtons = document.querySelectorAll(".scenario-button");
const resultCard = document.querySelector(".scenario-result");

function renderScenario(name) {
  const scenario = scenarios[name];
  if (!scenario) return;

  const question = document.getElementById("scenario-question");
  const status = document.getElementById("result-status");
  const icon = document.getElementById("result-icon");
  const answer = document.getElementById("scenario-answer");
  const source = document.getElementById("result-source");
  const trace = document.getElementById("scenario-trace");

  if (resultCard) resultCard.classList.add("is-changing");
  window.setTimeout(() => {
    if (question) question.textContent = scenario.question;
    if (status) {
      status.textContent = scenario.status;
      status.className = `result-status ${scenario.statusClass}`;
    }
    if (icon) {
      icon.textContent = scenario.icon;
      icon.className = `result-icon ${scenario.iconClass}`.trim();
    }
    if (answer) answer.textContent = scenario.answer;
    if (source) {
      source.replaceChildren();
      const iconSpan = document.createElement("span");
      iconSpan.setAttribute("aria-hidden", "true");
      iconSpan.textContent = scenario.source === "No source returned" ? "—" : "▤";
      const sourceName = document.createElement("span");
      sourceName.textContent = scenario.source;
      const sourceNote = document.createElement("span");
      sourceNote.textContent = scenario.sourceNote;
      source.append(iconSpan, sourceName, sourceNote);
    }
    if (trace) {
      trace.replaceChildren();
      scenario.trace.forEach((step, index) => {
        const label = document.createElement("span");
        label.textContent = step;
        trace.append(label);
        if (index < scenario.trace.length - 1) {
          const arrow = document.createElement("b");
          arrow.setAttribute("aria-hidden", "true");
          arrow.textContent = "→";
          trace.append(arrow);
        }
      });
    }
    if (resultCard) resultCard.classList.remove("is-changing");
  }, 100);
}

scenarioButtons.forEach((button) => {
  button.addEventListener("click", () => {
    scenarioButtons.forEach((otherButton) => {
      const active = otherButton === button;
      otherButton.classList.toggle("is-active", active);
      otherButton.setAttribute("aria-pressed", String(active));
    });
    renderScenario(button.dataset.scenario);
  });
});
