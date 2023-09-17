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
    '.text1-animation',
    {
        opacity:0
    },
    {
        opacity:1,
        duration:0.1
    }
);

tl.fromTo(
    '.text2-animation',
    {
        opacity:0
    },
    {
        opacity:1,
        duration:0.1
    }
);

tl.fromTo(
    '.text3-animation',
    {
        opacity:0
    },
    {
        opacity:1,
        duration:0.1
    }
);

tl.fromTo(
    '.button1-animation',
    {
        opacity:0
    },
    {
        opacity:1,
        duration:0.1
    }
);


tl.fromTo(
    '.text-h1-custom',
    {
        x:-150,
        opacity:0
    },
    {
        x:0,
        opacity:1,
        duration:1
    }
);

tl.fromTo(
    '.text-h4-custom',
    {
        y:50,
        opacity:0
    },
    {
        y:0,
        opacity:1,
        duration:0.3
    }
);

tl.fromTo(
    '.text-h5-custom',
    {
        y:-50,
        opacity:0
    },
    {
        y:0,
        opacity:1,
        duration:0.3
    }
);

tl.fromTo(
    '.button2-animation',
    {
        y:-50,
        opacity:0
    },
    {
        y:0,
        opacity:1,
        duration:0.1
    }
);

tl.fromTo(
    '.button3-animation',
    {
        y:-50,
        opacity:0
    },
    {
        y:0,
        opacity:1,
        duration:0.1
    }
);

tl.fromTo(
    '.hero_bg',
    {
        opacity:0
    },
    {
        opacity:1,
        duration:0.8
    }
);

tl.fromTo(
    '.spaceplain_bg',
    {
        opacity:0
    },
    {
        opacity:0.6,
        duration:0.5
    }
);
