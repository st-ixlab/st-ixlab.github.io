import { highlightSearchTerm } from "./highlight-search-term.js";

document.addEventListener("DOMContentLoaded", function () {
  let currentTypeFilter = "all";

  // Cache data-pub-type on parent <li> elements
  document.querySelectorAll(".bibliography > li").forEach((li) => {
    const row = li.querySelector("[data-pub-type]");
    if (row) {
      li.setAttribute("data-pub-type", row.getAttribute("data-pub-type"));
    }
  });

  // actual bibsearch & type filtering logic
  const filterItems = (searchTerm) => {
    document.querySelectorAll(".bibliography, .unloaded").forEach((element) => element.classList.remove("unloaded"));

    // 1. Text search filtering
    if (searchTerm && searchTerm.trim() !== "") {
      if (CSS.highlights) {
        const nonMatchingElements = highlightSearchTerm({ search: searchTerm, selector: ".bibliography > li" });
        if (nonMatchingElements != null) {
          nonMatchingElements.forEach((element) => {
            element.classList.add("unloaded");
          });
        }
      } else {
        // Fallback for browsers without CSS highlights
        document.querySelectorAll(".bibliography > li").forEach((element) => {
          const text = element.innerText.toLowerCase();
          if (text.indexOf(searchTerm) === -1) {
            element.classList.add("unloaded");
          }
        });
      }
    } else {
      if (CSS.highlights) {
        CSS.highlights.delete("search");
      }
    }

    // 2. Publication type filtering (journal / conference)
    if (currentTypeFilter !== "all") {
      document.querySelectorAll(".bibliography > li").forEach((element) => {
        const pubType = element.getAttribute("data-pub-type");
        if (pubType !== currentTypeFilter) {
          element.classList.add("unloaded");
        }
      });
    }

    // 3. Update year headings visibility
    document.querySelectorAll("h2.bibliography").forEach(function (element) {
      let iterator = element.nextElementSibling; // get next sibling element after h2, which can be h3 or ol
      let hideFirstGroupingElement = true;
      // iterate until next group element (h2)
      while (iterator && iterator.tagName !== "H2") {
        if (iterator.tagName === "OL") {
          const ol = iterator;
          const unloadedSiblings = ol.querySelectorAll(":scope > li.unloaded");
          const totalSiblings = ol.querySelectorAll(":scope > li");

          if (unloadedSiblings.length === totalSiblings.length) {
            ol.previousElementSibling.classList.add("unloaded"); // Add '.unloaded' to previous element
            ol.classList.add("unloaded"); // Add '.unloaded' to OL itself
          } else {
            hideFirstGroupingElement = false;
          }
        }
        iterator = iterator.nextElementSibling;
      }
      // Add unloaded class to first grouping element if no item left
      if (hideFirstGroupingElement) {
        element.classList.add("unloaded");
      }
    });

    // 4. Update year sidebar navigation links
    document.querySelectorAll("#year-sidebar-list li").forEach(function (li) {
      const link = li.querySelector("a");
      const targetId = link ? link.getAttribute("href")?.substring(1) : null;
      if (targetId) {
        const target = document.getElementById(targetId);
        if (target && target.classList.contains("unloaded")) {
          li.classList.add("unloaded");
        } else {
          li.classList.remove("unloaded");
        }
      }
    });
  };

  // Button filter click listeners
  document.querySelectorAll(".pub-filter-group button").forEach((button) => {
    button.addEventListener("click", function () {
      document.querySelectorAll(".pub-filter-group button").forEach((btn) => btn.classList.remove("active"));
      this.classList.add("active");
      currentTypeFilter = this.getAttribute("data-filter") || "all";
      const searchInput = document.getElementById("bibsearch");
      const searchTerm = searchInput ? searchInput.value.toLowerCase() : "";
      filterItems(searchTerm);
    });
  });

  const updateInputField = () => {
    const hashValue = decodeURIComponent(window.location.hash.substring(1));
    const searchInput = document.getElementById("bibsearch");
    if (searchInput) {
      if (window.location.hash && !hashValue.startsWith("year-")) {
        searchInput.value = hashValue;
        filterItems(hashValue.toLowerCase());
      } else {
        filterItems(searchInput.value ? searchInput.value.toLowerCase() : "");
      }
    }
  };

  // Debounced search input
  let timeoutId;
  const searchInput = document.getElementById("bibsearch");
  if (searchInput) {
    searchInput.addEventListener("input", function () {
      clearTimeout(timeoutId);
      const searchTerm = this.value.toLowerCase();
      timeoutId = setTimeout(() => filterItems(searchTerm), 300);
    });
  }

  window.addEventListener("hashchange", updateInputField);
  updateInputField();
});
