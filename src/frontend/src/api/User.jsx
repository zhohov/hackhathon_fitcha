import axios from "axios"

const RegisterUser = async (user) => {
    try {
        const { data } = await axios.post('localhost:8000/api/v1/user/create_user/', user)
        return data.user
    } catch {
        return 'failed'
    }
}

const LoginUser = async (username, email, password) => {
    const { data } = await axios.post(
        'localhost:8000/api/v1/user/login_user/', {
            username: username,
            email: email,
            hashed_password: password
        }
    )
    
    return data.id
}

const VerifyPassword = async (username, access, refresh) => {
    const { data } = await axios.post(
        'localhost:8000/api/v1/user/verify_token/', {
            username: username,
            access_token: access,
            refresh_token: refresh,
        }
    )
    return data
}
