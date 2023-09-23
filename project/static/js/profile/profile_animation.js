function startAnimationProfile(){
    const tl = gsap.timeline();
    
    tl.fromTo(
        '.hero_bg',
        {
            opacity:0
        },
        {
            opacity:0.05,
            duration:0.8
        }
    );
    
    tl.fromTo(
        '.spaceplain_bg',
        {
            opacity:0
        },
        {
            opacity:0.05,
            duration:0.5
        }
    );
}

startAnimationProfile();