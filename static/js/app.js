document.addEventListener('DOMContentLoaded', () => {
  const dropArea = document.getElementById('drop-area');
  const fileInput = document.getElementById('file-input');
  const fileList = document.getElementById('file-list');
  const uploadForm = document.getElementById('upload-form');
  const docsContainer = document.getElementById('docs-container');

  // Keep track of files selected across multiple interactions
  const selectedFiles = new DataTransfer();

  function fetchFiles() {
    fetch('/files')
      .then(r => r.json())
      .then(files => {
        docsContainer.innerHTML = '';
        const count = document.getElementById('docs-count');
        count.textContent = files.length;
        files.forEach(f => {
          const li = document.createElement('li');
          const date = new Date(f.date).toLocaleString();
          li.textContent = `${f.name} - ${date}`;
          docsContainer.appendChild(li);
        });
      });
  }

  if (dropArea) {
    ['dragenter', 'dragover'].forEach(evt => {
      dropArea.addEventListener(evt, e => {
        e.preventDefault();
        dropArea.classList.add('active');
      });
    });

    ['dragleave', 'drop'].forEach(evt => {
      dropArea.addEventListener(evt, e => {
        e.preventDefault();
        dropArea.classList.remove('active');
      });
    });

    dropArea.addEventListener('drop', e => {
      const files = e.dataTransfer.files;
      addFiles(files);
    });

    dropArea.addEventListener('click', () => fileInput.click());
  }

  function addFiles(files) {
    Array.from(files).forEach(f => selectedFiles.items.add(f));
    fileInput.files = selectedFiles.files;
    showSelectedFiles();
  }

  function showSelectedFiles() {
    fileList.innerHTML = '';
    Array.from(selectedFiles.files).forEach(f => {
      const li = document.createElement('li');
      li.textContent = f.name;
      fileList.appendChild(li);
    });
  }

  if (fileInput) {
    fileInput.addEventListener('change', e => {
      addFiles(e.target.files);
      // reset input so the same file can be selected again if needed
      e.target.value = '';
    });
  }

  if (uploadForm) {
    uploadForm.addEventListener('submit', e => {
      e.preventDefault();
      const formData = new FormData(uploadForm);
      fetch('/', { method: 'POST', body: formData })
        .then(resp => resp.text())
        .then(html => {
          document.body.innerHTML = html;
          fetchFiles();
        });
    });
  }

  fetchFiles();
});
