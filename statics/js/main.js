$(document).ready(function () {
  $(".upload-area").click(function () {
    $("#upload-input").trigger("click");
  });

  $("#upload-input").change((event) => {
    if (event.target.files) {
      let filesAmount = event.target.files.length;
      $(".upload-img").html("");

      for (let i = 0; i < filesAmount; i++) {
        let reader = new FileReader();
        reader.onload = function (event) {
          let html = `
            <div class = 'uploaded-img'>
            <img src = "${event.target.result}" width='100px' height='100px'>
            <button type = "button" class = "remove-btn">
            <i class = "fas fa-times"></i>
            </button>
            </div>
            `;
          $(".upload-img").append(html);
        };
        reader.readAsDataURL(event.target.files[i]);
      }

      $(".upload-info-value").text(filesAmount);
      $(".upload-img").css("padding", "20px");
    }
  });

  $(window).click(function (event) {
    if ($(event.target).hasClass("remove-btn")) {
      $(event.target).parent().remove();
    } else if ($(event.target).parent().hasClass("remove-btn")) {
      $(event.target).parent().parent().remove();
    }
  });
  $(document).on("click", ".remove-btn", function () {
    let imageContainer = $(this).closest(".uploaded-img");
    let imageUrl = imageContainer.find("img").attr("src");

    // Remove the image container from the DOM
    imageContainer.remove();

    // Send a request to the server to delete the corresponding file
    $.ajax({
      url: "/delete_image/", // Replace with the URL that handles image deletion in your Django view
      type: "POST",
      data: {
        image_url: imageUrl,
      },
      success: function (response) {
        console.log("Image deleted successfully.");
      },
      error: function (xhr, status, error) {
        console.log("Error deleting image:", error);
      },
    });

    let filesAmount = $(".uploaded-img").length;
    $(".upload-info-value").text(filesAmount);
  });
});
