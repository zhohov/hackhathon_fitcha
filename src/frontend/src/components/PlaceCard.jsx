import { useEffect, useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

const PlaceCard = () => {
    const router = useNavigate();

    const [places, setPlaces] = useState([]);
    

    const get_places = async() => {
        const response = await axios.get(
            'http://localhost:8000/api/v1/place/all_places'
        )
        setPlaces(response.data)
    }


    useEffect(() => {
        get_places()
    }, [])


    return(
        <div>
            {places.map((place) => 
                <div class="card m-4">
                        <img src={place.imgURL} class="card" alt="..."/>
                        <div class="d-flex justify-content-evenly">
                            <div class="position-absolute bottom-0 start-0">
                                <button type="button" class="btn btn-light m-3 btn-style">{place.name}</button>
                            </div>
                            <div class="position-absolute bottom-0 end-0">
                                <button type="button" class="btn btn-light m-3 btn-style" onClick={() => router('place/'+place.id)}>+</button>
                            </div>
                        </div>
                </div>
            )}
        </div>
    )
}

export default PlaceCard;
