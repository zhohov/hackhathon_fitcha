import image from '../static/images/16.png';
import image2 from './strelka.png';

function Folder(){
    return(
        <div class="folder card m-4" style={{height: '210px'}}>
            <div class="card-body">
                <h1 class="display-5 m-0 fw-normal" style={{lineHeight: '35px'}}>папка</h1>
                <p class="cards-subtitle" style={{maxWidth: '25ch'}}>mnbfbfbf bjfgfd bjxfgbjfgb jjbfg jbffd</p>
                <img src={image} class="position-absolute bottom-0 end-0" style={{width: '200px'}}/>
                <img src={image2} class="m-4 position-absolute bottom-0 start-0" style={{width: '50px'}}/>
            </div>
        </div>
    )
}

export default Folder;