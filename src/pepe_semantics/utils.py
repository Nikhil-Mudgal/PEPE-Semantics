from IPython.display import HTML


def visualize_giphy_gif(giphy_link):    
    return HTML(f"""
        <video autoplay loop muted>
            <source src="{giphy_link}" type="video/mp4" />
        </video>
    """)
