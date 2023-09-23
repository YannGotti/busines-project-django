function startAnimationAuth(){
    const tl = gsap.timeline();

    tl.fromTo(
        '.logo-animation',
        {
            y:-100,
            opacity:0
        },
        {
            y:0,
            opacity:1,
            duration:0.5
        }
    );
    
    tl.fromTo(
        '.text-h6-custom',
        {
            y:-100,
            opacity:0
        },
        {
            y:0,
            opacity:1,
            duration:0.2
        }
    );
    
    tl.fromTo(
        '.register-button',
        {
            y:-100,
            opacity:0
        },
        {
            y:0,
            opacity:1,
            duration:0.2
        }
    );
    
    
    tl.fromTo(
        '.form-animation',
        {
            y:-100,
            opacity:0
        },
        {
            y:0,
            opacity:1,
            duration:0.5
        }
    );
    
    tl.fromTo(
        '.hero_bg',
        {
            opacity:0
        },
        {
            opacity:0.2,
            duration:0.8
        }
    );
    
    tl.fromTo(
        '.spaceplain_bg',
        {
            opacity:0
        },
        {
            opacity:0.2,
            duration:0.5
        }
    );
}

startAnimationAuth();