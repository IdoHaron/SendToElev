class ImageCanvasManagement{
    constructor(){
        this.pointer_to_canvas = new fabric.Canvas("edit_image_canvas");
    }

    clear_canvas(){
        const context = canvas_pointer.getContext('2d');
        console.log("CLEAR!!!");
        context.clearRect(0, 0, canvas_pointer.width, canvas_pointer.height);

    }
    resize_canvas(wanted_width, wanted_height) {
        canvas_pointer.width= wanted_width;
        canvas_pointer.height = wanted_height;
    }
    convert_to_hex(){
        return canvas_pointer.toDataURL();
    }
    upload_image_to_canvas(image_encoding){
        ImageCanvasManagement.clear_canvas(canvas_pointer);
        const ctx = canvas_pointer.getContext("2d");
        var background = new Image();
        background.src = image_encoding;
        background.onload  = ()=>{
            ImageCanvasManagement.resize_canvas(canvas_pointer, background.naturalWidth, background.naturalHeight);
            ctx.drawImage(background, 0, 0);
        }
    }
    add_text_to_canvas(wanted_text, options){
        const text = new fabric.Text(wanted_text, options);
        this.pointer_to_canvas.add(text)
    }
}
