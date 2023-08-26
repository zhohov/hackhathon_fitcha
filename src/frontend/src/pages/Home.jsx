import Navbar from "../components/Navbar";
import PlaceCard from "../components/PlaceCard";
import Cards from "../components/Cards";
import Tags from "../components/Tags";
import MainCard from "../components/MainCard";

function Home(){
    return(
        <div>
            <MainCard />
            <Cards />
            <Tags />
            <PlaceCard />
        </div>
    )
}

export default Home;