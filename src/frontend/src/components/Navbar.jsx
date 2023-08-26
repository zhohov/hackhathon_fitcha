import axios from "axios";
import React, {useEffect, useState} from "react";
import { Link } from "react-router-dom";

const Navbar = () => {
    const [tags, setTags] = useState([]);
    const [cities, setCities] = useState([]);

    const get_tags = async () => {
        const response = await axios.get('http://localhost:8000/api/v1/tag/get_tags')
        setTags(response.data)
    }

    const get_cities = async () => {
        const response2 = await axios.get('http://localhost:8000/api/v1/city/get_cities')
        setCities(response2.data)
    }

    useEffect(() => {
        get_tags();
        get_cities()
    }, [])


    return(
        <nav class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container-fluid">
            <Link class="navbar-brand" to='/'>puzzle</Link>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                    <li class="nav-item">
                        <Link class="nav-link active" aria-current="page" to='/'>главная</Link>
                    </li>
                    <li class="nav-item">
                        <Link class="nav-link" to='/'>профиль</Link>
                    </li>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                            места
                        </a>
                        <ul class="dropdown-menu">
                            {tags.map((tag) => 
                                <li><Link class="dropdown-item" to='/'>{tag.name}</Link></li>
                            )}
                        </ul>
                    </li>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                            города
                        </a>
                        <ul class="dropdown-menu">
                            {cities.map((city) => 
                                <li><Link class="dropdown-item" to='/'>{city.name}</Link></li>
                            )}
                        </ul>
                    </li>
                </ul>
            </div>
        </div>
        </nav>
    )
}

export default Navbar;
