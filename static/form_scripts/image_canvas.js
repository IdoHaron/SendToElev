class ImageCanvasManagement{
    static pointer_to_canvas = "edit_image_canvas";
    static clear_canvas(canvas_pointer){
        const context = canvas_pointer.getContext('2d');
        console.log("CLEAR!!!");
        context.clearRect(0, 0, canvas_pointer.width, canvas_pointer.height);

    }
    static resize_canvas(canvas_pointer, wanted_width, wanted_height) {
        canvas_pointer.width= wanted_width;
        canvas_pointer.height = wanted_height;
    }
    static convert_to_hex(canvas_pointer){
        return canvas_pointer.toDataURL();
    }
    static upload_image_to_canvas(canvas_pointer, image_encoding){
        ImageCanvasManagement.clear_canvas(canvas_pointer);
        const ctx = canvas_pointer.getContext("2d");
        var background = new Image();
        background.src = image_encoding;
        background.onload  = ()=>{
            ImageCanvasManagement.resize_canvas(canvas_pointer, background.naturalWidth, background.naturalHeight);
            ctx.drawImage(background, 0, 0);
        }
    }
}
