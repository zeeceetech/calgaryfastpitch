// Load HTML includes
function loadIncludes() {
	// Load sponsors section
	const sponsorsPlaceholder = document.getElementById('sponsors-placeholder');
	if (sponsorsPlaceholder) {
		fetch('/includes/sponsors.html')
			.then(response => response.text())
			.then(data => {
				sponsorsPlaceholder.outerHTML = data;
			})
			.catch(error => console.error('Error loading sponsors:', error));
	}

	// Load footer section
	const footerPlaceholder = document.getElementById('footer-placeholder');
	if (footerPlaceholder) {
		fetch('/includes/footer.html')
			.then(response => response.text())
			.then(data => {
				footerPlaceholder.outerHTML = data;
			})
			.catch(error => console.error('Error loading footer:', error));
	}
}

// Load includes when DOM is ready
if (document.readyState === 'loading') {
	document.addEventListener('DOMContentLoaded', loadIncludes);
} else {
	loadIncludes();
}
