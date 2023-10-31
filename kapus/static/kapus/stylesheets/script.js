const webcam = document.getElementById('webcam');
const canvas = document.getElementById('canvas');
const startCamera = document.getElementById('startCamera');
const capturePhoto = document.getElementById('capturePhoto');
const retakePhoto = document.getElementById('retakePhoto');
const photoInput = document.getElementById('photoInput');
const capturedPhoto = document.getElementById('capturedPhoto');
const descriptionForm = document.getElementById('descriptionForm');
const inputPhoto = document.getElementById('photo')

let mediaStream;

startCamera.addEventListener('click', async () => {
    mediaStream = await navigator.mediaDevices.getUserMedia({ video: true });
    webcam.srcObject = mediaStream;
    webcam.style.display = 'block';
    startCamera.style.display = 'none';
    capturePhoto.style.display = 'inline';
});

capturePhoto.addEventListener('click', () => {
    canvas.width = webcam.videoWidth;
    canvas.height = webcam.videoHeight;
    canvas.getContext('2d').drawImage(webcam, 0, 0);
    capturedPhoto.src = canvas.toDataURL('image/jpeg');
    webcam.style.display = "none";
    capturedPhoto.style.display = 'block'; //wystawione
    capturePhoto.style.display = 'none';
    retakePhoto.style.display = 'inline';
    mediaStream.getTracks().forEach((track) => track.stop()); // Close the camera stream
    inputPhoto.value = "img_55"
});

retakePhoto.addEventListener('click', async () => {
    mediaStream = await navigator.mediaDevices.getUserMedia({ video: true });
    webcam.srcObject = mediaStream;
    webcam.style.display = 'block';
    capturedPhoto.style.display = 'none';
    capturePhoto.style.display = 'inline';
    retakePhoto.style.display = 'none';
});

photoInput.addEventListener('change', () => {
    const selectedFile = photoInput.files[0];
    console.log("selected file", selectedFile)
    const reader = new FileReader();
    reader.onload = (e) => {
        console.log(e.target)
        capturedPhoto.src = e.target.result;
        if(mediaStream){
            mediaStream.getTracks().forEach((track) => track.stop());
        }
        webcam.style.display = "none";
        capturedPhoto.style.display = 'block';
    };
    reader.readAsDataURL(selectedFile);
});

