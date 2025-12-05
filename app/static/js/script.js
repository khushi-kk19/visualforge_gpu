let currentDetections = [];
let currentImageFile = null;

// Upload area drag and drop
const uploadArea = document.getElementById('uploadArea');
const imageInput = document.getElementById('imageInput');
const previewSection = document.getElementById('previewSection');
const outputSection = document.getElementById('outputSection');
const loadingSpinner = document.getElementById('loadingSpinner');

uploadArea.addEventListener('click', () => imageInput.click());

uploadArea.addEventListener('dragover', (e) => {
    e.preventDefault();
    uploadArea.classList.add('drag-over');
});

uploadArea.addEventListener('dragleave', () => {
    uploadArea.classList.remove('drag-over');
});

uploadArea.addEventListener('drop', (e) => {
    e.preventDefault();
    uploadArea.classList.remove('drag-over');
    const files = e.dataTransfer.files;
    if (files.length > 0) {
        handleImageUpload(files[0]);
    }
});

imageInput.addEventListener('change', (e) => {
    if (e.target.files.length > 0) {
        handleImageUpload(e.target.files[0]);
    }
});

function handleImageUpload(file) {
    currentImageFile = file;
    
    // Show preview
    const reader = new FileReader();
    reader.onload = (e) => {
        document.getElementById('previewImage').src = e.target.result;
    };
    reader.readAsDataURL(file);

    // Detect objects
    detectObjects(file);
}

function detectObjects(file) {
    const formData = new FormData();
    formData.append('image', file);

    showLoading(true);

    fetch('/detect', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        showLoading(false);
        currentDetections = data.detections;
        
        // Display detected objects
        const objectsSet = new Set(data.detected_objects);
        const objectsHTML = Array.from(objectsSet)
            .map(obj => `<span class="object-badge">${obj}</span>`)
            .join('');
        document.getElementById('detectedObjects').innerHTML = objectsHTML;

        // Populate dropdowns
        const objectOptions = Array.from(objectsSet)
            .map(obj => `<option value="${obj}">${obj}</option>`)
            .join('');
        
        document.getElementById('removeSelect').innerHTML = '<option value="">Select object to remove</option>' + objectOptions;
        document.getElementById('replaceSelect').innerHTML = '<option value="">Select object to replace</option>' + objectOptions;

        // Show editor tools
        uploadArea.style.display = 'none';
        previewSection.style.display = 'grid';
        outputSection.style.display = 'none';
    })
    .catch(error => {
        showLoading(false);
        alert('Error detecting objects: ' + error);
    });
}

function removeObject() {
    const objectToRemove = document.getElementById('removeSelect').value;
    
    if (!objectToRemove) {
        alert('Please select an object to remove');
        return;
    }

    const formData = new FormData();
    formData.append('image', currentImageFile);
    formData.append('object', objectToRemove);

    showLoading(true);

    fetch('/remove', {
        method: 'POST',
        body: formData
    })
    .then(response => response.blob())
    .then(blob => {
        showLoading(false);
        displayOutput(blob);
    })
    .catch(error => {
        showLoading(false);
        alert('Error removing object: ' + error);
    });
}

function replaceObject() {
    const objectToReplace = document.getElementById('replaceSelect').value;
    const replaceWith = document.getElementById('replaceWith').value;

    if (!objectToReplace || !replaceWith) {
        alert('Please select object and enter replacement');
        return;
    }

    const formData = new FormData();
    formData.append('image', currentImageFile);
    formData.append('old', objectToReplace);
    formData.append('new', replaceWith);

    showLoading(true);

    fetch('/replace', {
        method: 'POST',
        body: formData
    })
    .then(response => response.blob())
    .then(blob => {
        showLoading(false);
        displayOutput(blob);
    })
    .catch(error => {
        showLoading(false);
        alert('Error replacing object: ' + error);
    });
}

function addObject() {
    const newObject = document.getElementById('addObject').value;

    if (!newObject) {
        alert('Please enter object name');
        return;
    }

    const formData = new FormData();
    formData.append('image', currentImageFile);
    formData.append('object', newObject);

    showLoading(true);

    fetch('/add', {
        method: 'POST',
        body: formData
    })
    .then(response => response.blob())
    .then(blob => {
        showLoading(false);
        displayOutput(blob);
    })
    .catch(error => {
        showLoading(false);
        alert('Error adding object: ' + error);
    });
}

function changeStyle() {
    const style = document.getElementById('styleSelect').value;

    if (!style) {
        alert('Please select a style');
        return;
    }

    const formData = new FormData();
    formData.append('image', currentImageFile);
    formData.append('style', style);

    showLoading(true);

    fetch('/style', {
        method: 'POST',
        body: formData
    })
    .then(response => response.blob())
    .then(blob => {
        showLoading(false);
        displayOutput(blob);
    })
    .catch(error => {
        showLoading(false);
        alert('Error applying style: ' + error);
    });
}

function displayOutput(blob) {
    const url = URL.createObjectURL(blob);
    document.getElementById('outputImage').src = url;
    document.getElementById('downloadBtn').href = url;
    document.getElementById('downloadBtn').download = 'visualforge-output.png';
    
    previewSection.style.display = 'none';
    outputSection.style.display = 'block';
    
    // Scroll to output
    outputSection.scrollIntoView({ behavior: 'smooth' });
}

function resetEditor() {
    uploadArea.style.display = 'block';
    previewSection.style.display = 'none';
    outputSection.style.display = 'none';
    currentImageFile = null;
    currentDetections = [];
    imageInput.value = '';
    
    document.getElementById('replaceWith').value = '';
    document.getElementById('addObject').value = '';
}

function showLoading(show) {
    if (show) {
        loadingSpinner.classList.add('active');
    } else {
        loadingSpinner.classList.remove('active');
    }
}

function scrollToEditor() {
    document.getElementById('editor').scrollIntoView({ behavior: 'smooth' });
}
