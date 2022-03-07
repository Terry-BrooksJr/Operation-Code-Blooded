import react from 'react'
import LottieView from '@lottiefiles/react-lottie-player'
import { View, Stylesheet } from 'react-native'


'
const appLoader = () => {
return ( <
    View style = {
        [Stylesheet.absoluteFillObjectl, styles.container]
    } >
    <
    LottieView source = { require('../96393-loader-desygner.json')}
    autoplay loop / >
    <
    /View>
)
};
const styles = Stylesheet.create({
    container: {
        justifyContent: 'center',x
        alignItems: 'center',
        backgroundColor: 'rgba(0,0,0,0.3)',
        zindex: 1
    }
}) 