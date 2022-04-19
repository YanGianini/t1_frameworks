from theater.models import Categoria, Video

categoria1 = Categoria('Humor', 'Videos de Comedia', 'laughing.png')
categoria2 = Categoria('Automobilistico', 'Vrum Vrum','car.png')
categoria3 = Categoria('Games', 'Video games','joystick.png')

categorias = [categoria1, categoria2, categoria3]

categoria3.add_video(Video(1, "Elden Ring", "https://www.youtube.com/embed/E3Huy2cdih0", "elden.jpg", "Trailer do jogo Elden Ring", 229000, 10121042, '10 de jun. de 2021'))
categoria3.add_video(Video(2, "Lego Star Wars", "https://www.youtube.com/embed/AzjUuIMs5N0", "lego.jpg", "Trailer do jogo Lego Star Wars - Skywalker saga", 3000, 19.032, '5 de abr. de 2022'))
categoria3.add_video(Video(3, "VALORANT", "https://www.youtube.com/embed/h1Kp9x_ADZw", "val.jfif", "Trailer do jogo Valorant após lançamento de seu Beta", 31000, 715686, '29 de mai. de 2020'))

categoria1.add_video(Video(4, "Encanto", "https://www.youtube.com/embed/GsJd_o97h5U", "encanto.jpeg", "Encontre a sua magia. 🕯✨🦋 Assista ao novo trailer de Encanto da Disney", 16000, 1057674, '29 de set. de 2021'))
categoria1.add_video(Video(5, "Sonic 2", "https://www.youtube.com/embed/47r8FXYZWNU", "sonic.jfif", "O mundo precisava de um herói, recebemos um ouriço. Dotado de incrível velocidade, Sonic ", 247000, 27664055, '14 de mar. de 2022'))
categoria1.add_video(Video(6, "The Hangover", "https://www.youtube.com/embed/jOQMBfWMMsU", "hang.jfif", "Trailer teaser do filme 'Se Beber Não Case', comédia do diretor Todd Phillips, com Bradley Cooper, Heather Graham, Justin Bartha, Ed Helms e Zach Galifianaki.", 647, 278762, '16 de mar. de 2009'))


