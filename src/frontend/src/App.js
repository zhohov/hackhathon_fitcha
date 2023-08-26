import logo from './logo.svg';
import './App.css';
import {BrowserRouter, Route, Routes} from 'react-router-dom';
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import Login from './pages/Login';
import Home from './pages/Home';
import Registration from './pages/Registration';
import SortedList from './pages/SortedList';

function App() {

	return (
		<div className="App">
			<BrowserRouter>
				<Navbar />
				<Routes>
					<Route path='/' element={<Home />}></Route>
					<Route path='/signin' element={<Login />}></Route>
					<Route path='/signup' element={<Registration />}></Route>
					<Route path='/tags/:tag_id' element={<SortedList />}></Route>
				</Routes>
				<Footer />
			</BrowserRouter>
		</div>
	);
}

export default App;
