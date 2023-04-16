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
}
