import PlaceCard from "../components/PlaceCard";

const Home = () => {

    return (
        <div className="">
            <div class="grid text-left head">
                <div class="px-2 pt-5 g-col-12">
                    <h1 class="display-5 mt-5-sm pt-5">Путешествуй по<br />городу вместе с<br /><mark id='logo'>Puzzle</mark></h1>
                    <div class="bottom-0 pb-0">
                        <button type="submit" class=" mt-5 btn btn-primary">читать журнал →</button>
                    </div>      
                </div>
            </div>

            <hr className="border-3 mt-5" />

            <div class='my-5'>
                <small>о журнале</small> <br /><br />
                <p class="lead">Погрузитесь в захватывающий мир искусственного интеллекта с AI magazine. Узнайте о последних тенденциях, открытиях и вдохновляющих примерах применения ИИ во всех сферах жизни. Станьте свидетелем прорывов и открытий, которые меняют мир. Присоединяйтесь к нам и расширьте свои границы с AI magazine!</p>
            </div>
            <PlaceCard />
        </div>
    )
}

export default Home;