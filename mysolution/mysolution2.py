import igraph as ig

def main():
    print("II Grafy preferential attachment (Barabási-Albert")

    # 2. Wygeneruj graf wedle modelu Barabási-Albert z tysiącem węzłów
    g = ig.Graph.Barabasi(n=1000, m=1)

    # 3. Zwizualizuj graf layoutem Fruchterman & Reingold
    print("\n[3] Generowanie wizualizacji...")
    layout = g.layout("fr")
    
    visual_style = {
        "vertex_size": 7,
        "vertex_color": "darkgreen",
        "edge_width": 2,
        "layout": layout,
        "bbox": (800, 800),
        "margin": 50
    }
    
    # Wizualizacja zapisana w pliku: 
    ig.plot(g, "mysolution/2_3_graph_visualization.png", **visual_style)
    print("Wizualizację zapisano jako mysolution/2_3_graph_visualization.png")

    #  4. Znajdź najbardziej centralny węzeł według miary betweenness, jaki ma numer?
    betweenness_values = g.betweenness()
    max_val = max(betweenness_values) # Szukamy maksimum, bo betweenness mierzy centralność węzła w grafie
    max_idx = betweenness_values.index(max_val) # Odpowiedź: 0 (zazwyczaj najbardziej centralny to jeden z pierwszych węzłów)

    print(f"\n[4] Najbardziej centralny węzeł:")
    print(f"Numer węzła (indeks): {max_idx}")
    print(f"Wartość betweenness: {max_val}")

    #  5. Jaka jest średnica grafu?
    diameter = g.diameter()
    print(f"\n[5] Średnica grafu: {diameter}")

    #  6. W komentarzu napisz czym różnią się grafy Barabási-Albert i Erdős-Rényi.
    """
    Główne różnice między grafami:
    
    1. Rozkład stopni:
       - Erdős-Rényi (ER): Rozkład przypomina krzywą dzwonową. 
         Większość węzłów ma podobną liczbę połączeń (średnią).
       - Barabási-Albert (BA): Rozkład potęgowy (Power Law). 
         Istnieje wiele węzłów o bardzo małym stopniu i niewielka ilość potężnych wieżchołków o ogromnej liczbie połączeń (hubów). 
         Struktura tego grafu przypomina drzewo, które ma wiele liści (węzłów o niskim stopniu).
         Taka struktura grafu bardziej odnosi się do rzeczywistości, bo przypomina na przykład strukturę internetu czy sieci bilogicznych,
         gdzie też występują huby.
         
    2. Mechanizm tworzenia:
       - ER: Połączenia są całkowicie losowe i niezależne.
       - BA: Działa mechanizm "preferential attachment" (bogaci się bogacą). 
         Dlatego też najbardziej centralny węzeł to zazwyczaj jeden z pierwszych.
         Nowe węzły chętniej łączą się z tymi, które już mają dużo połączeń.
    """


if __name__ == "__main__":
    main()