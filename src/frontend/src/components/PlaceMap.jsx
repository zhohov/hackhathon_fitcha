import React from "react";
import { YMaps, Map, Placemark, Polyline} from '@pbe/react-yandex-maps';


const PlaceMap = () => {

    return (
        <div class="m-4">
            <YMaps
                query={{
                    ns: "use-load-option",
                    load: "Map,Placemark,control.ZoomControl,control.FullscreenControl,geoObject.addon.balloon",
                }}
                >
                <Map
                    class="map-block"
                    width='100%'
                    defaultState={{
                    center: [55.75, 37.57],
                    zoom: 13,
                    controls: ["zoomControl", "fullscreenControl"],
                    }}
                >
                    <Placemark
                    defaultGeometry={[55.75, 37.57]}
                    properties={{
                        balloonContentBody:
                        "This is balloon loaded by the Yandex.Maps API module system",
                    }}
                    />

                    <Placemark
                    defaultGeometry={[55.7, 31.4]}
                    properties={{
                        balloonContentBody:
                        "This is balloon loaded by the Yandex.Maps API module system",
                    }}
                    />

                    <Placemark
                    defaultGeometry={[56.7, 30.4]}
                    properties={{
                        balloonContentBody:
                        "This is balloon loaded by the Yandex.Maps API module system",
                    }}
                    />
                    
                    
                    <Polyline
                    geometry={[
                        [55.8, 37.5],
                        [55.7, 31.4],
                        [56.7, 30.4],
                    ]}
                    options={{
                        strokeWidth: 5,
                    }}
                     />
                </Map>
            </YMaps>
        </div>
    )
    
}

export default PlaceMap;