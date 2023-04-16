const to_board_select = "board"
const board_form = "message_construct"

async function onload_body(){
    await sleep(10);
    const image_input_obj = document.getElementById(ImgSrcManagement.image_source_select_id);
    ImgSrcManagement.update_input_option(image_input_obj);
}

async function sumbit_editied_image(event){
    event.preventDefault();
    console.log("submited!!");
    const canvas_pointer = document.getElementById(ImageCanvasManagement.pointer_to_canvas);
    const canvas_to_hex = ImageCanvasManagement.convert_to_hex(canvas_pointer);
    const chosen_board = document.getElementById(to_board_select).value;
    const form_path =document.getElementById(board_form).action;
    // add support to form upload.
    NetworkUtils.send_request(form_path, "POST", JSON.stringify({"image": canvas_to_hex, "destination":chosen_board}))

};


async function on_change_template(element_pointer){
    const current_template =element_pointer.value;
    if(current_template == 0){
        return;
    }
    const image_encoding = NetworkUtils.request_from_route("templae/"+current_template);
    const image_canvas = document.getElementById(ImageCanvasManagement.pointer_to_canvas)
    ImageCanvasManagement.upload_image_to_canvas(image_canvas, image_encoding);
}
