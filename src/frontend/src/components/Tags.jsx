import axios from "axios";
import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";

const Tags = () => {
    const [tags, setTag] = useState([]);
    const navigate = useNavigate();
    

    const get_tags = async() => {
        const response = await axios.get(
            'http://localhost:8000/api/v1/tag/get_tags/'
        )
        setTag(response.data)
    }


    useEffect(() => {
        get_tags()
    }, [])

    return(
        <div className="m-4">
            {tags.map((tag) =>
                <button type="button" class="ms-2 btn btn-outline-light btn-style" onClick={() => navigate('tags/'+tag.id)}>{tag.name}</button>
            )}
        </div>
    )
}

export default Tags;