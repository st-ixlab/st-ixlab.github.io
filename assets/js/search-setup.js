// Defer theme determination and element selection to ensure dependencies are loaded
(function() {
  try {
    const ninjaKeys = document.querySelector("ninja-keys");
    if (!ninjaKeys) return;

    // Check if determineComputedTheme is available (it might not be if dark mode is disabled)
    let searchTheme = 'light';
    if (typeof determineComputedTheme === 'function') {
      searchTheme = determineComputedTheme();
    }

    if (searchTheme === "dark") {
      ninjaKeys.classList.add("dark");
    } else {
      ninjaKeys.classList.remove("dark");
    }
  } catch (error) {
    console.error("Error initializing search theme:", error);
  }
})();

function openSearchModal() {
  // collapse navbarNav if expanded on mobile
  const $navbarNav = $("#navbarNav");
  if ($navbarNav.hasClass("show")) {
    $navbarNav.collapse("hide");
  }
  
  const ninjaKeys = document.querySelector("ninja-keys");
  if (ninjaKeys) {
    ninjaKeys.open();
  }
};
