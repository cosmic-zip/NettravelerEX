settings_sec = """
<section class="content-sec" id="settings">
    <style>
        .settings-wallpaper {
            display: grid;
            justify-content: center;
            grid-template-columns: repeat(auto-fit, 320px);
            width: calc(100vw - 390px);
            gap: 40px;
        }

        .settings-wallpaper-ctn {
            border-radius: 10px;
            text-align: center;
        }

        .settings-wallpaper-ctn:hover {
            position: relative;
            width: 350px;

        }

        .wallpaper-selector {
            border-radius: 10px;
            border: none;
            background: var(--warning);
            background-size: cover;
            width: 100%;
            height: 180px;
        }


        .bg-1 {
            background-image: url(assets/bg1.jpg);
        }

        .bg-2 {
            background-image: url(assets/bg2.jpg);
        }

        .bg-3 {
            background-image: url(assets/bg3.jpg);
        }

        .bg-4 {
            background-image: url(assets/bg4.jpg);
        }
        
        .bg-5 {
            background-image: url(assets/bg5.png);
        }
    </style>
    <div class="settings-container">

        <header class="sec-header">
            <span><em>Settings</em></span>
        </header>

        <div class="settings-wallpaper">
            <div class="settings-wallpaper-ctn" style="background-color: #b9921e;">
                <button class="wallpaper-selector bg-5" hx-on:click="
                                document.body.style.backgroundImage = 'url(assets/bg5.png)';
                                document.documentElement.style.setProperty('--text-color', 'aliceblue');
                                document.documentElement.style.setProperty('--ancient', '#d54f03');
                                document.documentElement.style.setProperty('--contrast', 'black');
                                document.documentElement.style.setProperty('--dk-ancient', '#5b4f0e');
                                document.documentElement.style.setProperty('--bg', '#666666');
                                document.documentElement.style.setProperty('--warning', 'rgba(0, 0, 0, 0.8)');
                                document.documentElement.style.setProperty('--error', 'rgba(108, 0, 0, 0.8)');
                                document.documentElement.style.setProperty('--ok', 'rgb(0, 116, 128)');
                                ">
                </button>
                <h3>Embers</h3>
            </div>

            <div class="settings-wallpaper-ctn" style="background-color: #8f1eb9;">
                <button class="wallpaper-selector bg-1" hx-on:click="
                                document.body.style.backgroundImage = 'url(assets/bg1.jpg)';
                                document.documentElement.style.setProperty('--text-color', 'aliceblue');
                                document.documentElement.style.setProperty('--ancient', '#8f1eb9');
                                document.documentElement.style.setProperty('--contrast', 'black');
                                document.documentElement.style.setProperty('--dk-ancient', '#460e5b');
                                document.documentElement.style.setProperty('--bg', '#666666');
                                document.documentElement.style.setProperty('--warning', 'rgba(58, 0, 74, 0.8)');
                                document.documentElement.style.setProperty('--error', 'rgba(108, 0, 0, 0.8)');
                                document.documentElement.style.setProperty('--ok', 'rgb(0, 116, 128)');
                                ">
                </button>
                <h3>Lucy</h3>
            </div>

            <div class="settings-wallpaper-ctn" style="background-color: #626262;">
                <button class="wallpaper-selector bg-2" hx-on:click="
                                document.body.style.backgroundImage = 'url(assets/bg2.jpg)';
                                document.documentElement.style.setProperty('--ancient', '#626262');
                                document.documentElement.style.setProperty('--contrast', 'black');
                                document.documentElement.style.setProperty('--dk-ancient', '#131313');
                                document.documentElement.style.setProperty('--warning', 'rgba(0, 0, 0, 0.8)');
                                ">
                </button>
                <h3>Cyberpunk 2077</h3>
            </div>

            <div class="settings-wallpaper-ctn" style="background-color: #c607fb;">
                <button class="wallpaper-selector bg-3" hx-on:click="document.body.style.backgroundImage = 'url(assets/bg3.jpg)';
                                document.documentElement.style.setProperty('--ancient', '#c607fb');
                                document.documentElement.style.setProperty('--contrast', 'black');
                                document.documentElement.style.setProperty('--dk-ancient', '#a40099');
                                document.documentElement.style.setProperty('--warning', 'rgba(0, 42, 140, 0.8)');">
                </button>
                <h3>Neko girl</h3>
            </div>

            <div class="settings-wallpaper-ctn" style="background-color: #31b91e;">
                <button class="wallpaper-selector bg-4" hx-on:click="document.body.style.backgroundImage = 'url(assets/bg4.jpg)';
                                document.documentElement.style.setProperty('--ancient', '#31b91e');
                                document.documentElement.style.setProperty('--contrast', 'black');
                                document.documentElement.style.setProperty('--dk-ancient', '#2b4a51');
                                document.documentElement.style.setProperty('--warning', 'rgba(9, 74, 0, 0.8)');">
                </button>
                <h3>Green dreams</h3>
            </div>




        </div>


    </div>
</section>
"""

settings = {
    "section": settings_sec,
    "buttom": '<button type="submit" class="sidebar-submit" onclick="toggleSection(\'settings\')">㊊ Settings</button>'
}
