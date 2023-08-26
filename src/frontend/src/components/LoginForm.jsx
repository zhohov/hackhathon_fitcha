import {React, useState} from "react";
import axios from "axios";
import { useNavigate, Link } from "react-router-dom";

const LoginForm = () => {
    const navigate = useNavigate();
    const [username, setUsername] = useState([]);
    const [password, setPassword] = useState([]);

    const submit = async (e) => {
        e.preventDefault();

        const user = {
            username: username,
            hashed_password: password,
        };

        try {
            const { data }  = await axios.post('http://localhost:8000/api/v1/user/login_user/', user);
            localStorage.clear();
            localStorage.setItem('access_token', data.access);  
            localStorage.setItem('refresh_token', data.refresh);
            axios.defaults.headers.common['Authorization'] = 'Bearer $(data.acsess)';
            try {
                const config = {
                    headers: {
                        Authorization: 'Bearer ' + localStorage.getItem('access_token'),
                    }
                }
                const { data } = await axios.get('http://localhost:8000/auth/users/me/', config);
                localStorage.setItem('username', data.username)
            } catch (e) {
                alert(e)
            }

            navigate('/');

        } catch (e) {
            alert(localStorage.getItem('access_token'), e)
        }
    }

    return (
        <div class="row justify-content-center pt-5">
            <h1 class='text-center'>AI magazine</h1>
            <form class="col-12 col-xl-4" text-center onSubmit={submit}>
                <p class='m-3'>Cздайте аккаунт для того, чтобы создавать свои маршруты</p>
                <div class="input-group mb-4">
                    <span class="input-group-text">@</span>
                    <div class="form-floating">
                        <input value={username} onChange={(e) => setUsername(e.target.value)} type="text" class="form-control" id="floatingInputGroup1" placeholder="Username" />
                        <label for="floatingInputGroup1">Username</label>
                    </div>
                </div>
                <div class="form-floating">
                    <input value={password} onChange={(e) => setPassword(e.target.value)} type="password" class="form-control" id="floatingPassword" placeholder="Password" />
                    <label for="floatingPassword">Password</label>
                </div>

                <div class="text-center m-4">
                    <button type="submit" class="btn btn-primary mb-2">Войти</button><br />
                    <small><Link to='/registration'>Еще нет аккаунта? Зарегистрироваться</Link><br></br></small>
                </div>      
            </form>
        </div>
    );
};

export default LoginForm;