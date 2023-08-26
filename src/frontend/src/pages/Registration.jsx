import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate, Link } from 'react-router-dom';

const Registration = () => {
    const navigate = useNavigate();
    const [email, setEmail] = useState([]);
    const [username, setUsername] = useState([]);
    const [password, setPassword] = useState([]);

    const submit = async (e) => {
        e.preventDefault();
        try {
            await axios.post('http://localhost:8000/api/v1/user/create_user/', {
                email: email,
                username: username,
                hashed_password: password, 
            })
            navigate('/')
        } catch (e) {
            alert(e)
        }
    }

    return (
        <div class='container-sm px-3 px-md-5 mt-5'>
            <div class="row justify-content-center text-center pt-5">
                <h1 class='text-center'>AI magazine</h1>
                <form class="col-12 col-xl-4" text-center onSubmit={submit}>
                    <p class='m-3'>Cздайте аккаунт для того, чтобы просматривать все выпуски журнала</p>
                    <div class="input-group mb-4">
                        <span class="input-group-text">@</span>
                        <div class="form-floating">
                            <input value={username} onChange={(e) => setUsername(e.target.value)} type="text" class="form-control" id="floatingInputGroup1" placeholder="Username" />
                            <label for="floatingInputGroup1">Username</label>
                        </div>
                    </div>
                    <div class="form-floating mb-4">
                        <input value={email} onChange={(e) => setEmail(e.target.value)} type="email" class="form-control" id="floatingInput" placeholder="name@example.com" />
                        <label for="floatingInput">Email address</label>
                    </div>
                    <div class="form-floating">
                        <input value={password} onChange={(e) => setPassword(e.target.value)} type="password" class="form-control" id="floatingPassword" placeholder="Password" />
                        <label for="floatingPassword">Password</label>
                    </div>

                    <div class="text-center m-4">
                        <button type="submit" class="btn btn-primary mb-2">Зарегистрироваться</button><br />
                        <small><Link to='/login'>Уже есть аккаунт? Войти</Link></small>
                    </div>      
                </form>
            </div>
        </div>
    );
};

export default Registration;