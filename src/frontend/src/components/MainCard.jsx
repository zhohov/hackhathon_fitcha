import image from "../static/images/5.png";

function MainCard(){
    return(
        <div class="folder card m-4" style={{height: '210px'}}>
            <div class="card-body">
                <h1 class="display-5 m-0 fw-normal" style={{lineHeight: '35px'}}>путешествуй<br/>вместе с<br/>puzzle</h1>
                <button type="button" class="mt-4 btn btn-dark btn-style">get started → </button>
                <img src={image} class="position-absolute bottom-0 end-0" style={{width: '200px'}}/>
            </div>
        </div>
    )
}

export default MainCard;