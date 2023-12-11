(() => {
    const width = 220;
    let height = 0;
    let streaming = false;
    let video = null;
    let canvas = null;
    let photo = null;
    let startbutton = null;
    let submitbutton = null;

    function startup() {
        video = document.getElementById("video");
        canvas = document.getElementById("canvas");
        photo = document.getElementById("photo");
        startbutton = document.getElementById("startbutton");
        submitbutton = document.getElementById("submitbutton");

        navigator.mediaDevices
            .getUserMedia({ video: true, audio: false })
            .then((stream) => {
                video.srcObject = stream;
                video.play();
            })
            .catch((err) => {
                console.error(`An error occurred: ${err}`);
            });

        video.addEventListener(
            "canplay",
            (ev) => {
                if (!streaming) {
                    height = video.videoHeight / (video.videoWidth / width);

                    if (isNaN(height)) {
                        height = width / (4 / 3);
                    }

                    video.setAttribute("width", width);
                    video.setAttribute("height", height);
                    canvas.setAttribute("width", width);
                    canvas.setAttribute("height", height);
                    streaming = true;
                }
            },
            false
        );

        startbutton.addEventListener(
            "click",
            (ev) => {
                takepicture();
                ev.preventDefault();
            },
            false
        );

        clearphoto();
    }

    function clearphoto() {
        const context = canvas.getContext("2d");
        context.fillStyle = "#AAA";
        context.fillRect(0, 0, canvas.width, canvas.height);

        const data = canvas.toDataURL("image/png");
        photo.setAttribute("src", data);
    }

    function takepicture() {
        const context = canvas.getContext("2d");
        if (width && height) {
            canvas.width = width;
            canvas.height = height;
            context.drawImage(video, 0, 0, width, height);

            const data = canvas.toDataURL("image/png");
            photo.setAttribute("src", data);

            // Add the captured image data to a hidden form field
            const hiddenField = document.getElementById("photo_data");
            hiddenField.value = data;

            // Send an AJAX request to the Django backend
            const form = document.getElementById("visitor-form");
            const formData = new FormData(form);
            
            // Include the CSRF token in the request headers
            const csrftoken = getCookie('YOUR_CSRF_TOKEN_COOKIE_NAME'); // Replace with your actual CSRF token cookie name
            
            fetch("/save-captured-photo/", {
                method: "POST",
                body: formData,
                headers: {
                    "X-CSRFToken": csrftoken, // Include the CSRF token in the request headers
                },
            })
                .then((response) => response.json())
                .then((data) => {
                    // Handle the response from the backend (e.g., show a success message)
                    console.log(data);
                })
                .catch((error) => {
                    console.error("Error:", error);
                });
        } else {
            clearphoto();
        }
    }

    window.addEventListener("load", startup, false);
})();



