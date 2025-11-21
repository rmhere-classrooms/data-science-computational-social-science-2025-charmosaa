import igraph as ig
import random
import matplotlib.pyplot as plt

def main():
    print("I Grafy losowe")

    # 2. Wygeneruj sieć Erdős-Rényi o stu wierzchołkach i prawdopodobieństwie krawędzi = 0.05
    g = ig.Graph.Erdos_Renyi(n=100, p=0.05)
    
    # 3. Wydrukuj podsumowanie grafu - czy graf jest ważony?
    print("\n[3] Podsumowanie grafu (przed wagami):")
    print(g.summary())
    is_weighted = g.is_weighted()
    print(f"Czy graf jest ważony? {'TAK' if is_weighted else 'NIE'}") # Odpowiedź: NIE

    # 4. Wylistuj wszystkie wierzchołki i krawędzie
    print("\n[4] Wierzchołki i krawędzie:")
    print(f"Lista wierzchołków: {list(range(g.vcount()))}")
    print(f"Lista krawędzi: {g.get_edgelist()}")

    # 5. Ustaw wagi wszystkich krawędzi na losowe z zakresu 0.01 do 1
    weights = [random.uniform(0.01, 1.0) for _ in range(g.ecount())]
    g.es['weight'] = weights

    # 6. Wydrukuj ponownie podsumowanie grafu - czy teraz graf jest ważony?
    print("\n[6] Podsumowanie grafu (po dodaniu wag):")
    print(g.summary())
    is_weighted_now = g.is_weighted()
    print(f"Czy graf jest ważony? {'TAK' if is_weighted_now else 'NIE'}") # Odpowiedź: TAK

    # 7. Jaki jest stopień każdego węzła? Następnie stwórz histogram stopni węzłów
    degrees = g.degree()
    print(f"\n[7] Stopnie węzłów: {degrees}") # Odpowiedź: [3, 2, 3, 6, 4, 3, 5, 9, 5, 9, 12, 5, 2, 4, 1, 9, 4, 4, 4, 5, 2, 3, 4, 5, 5, 7, 3, 6, 6, 7, 5, 1, 3, 5, 8, 6, 6, 7, 4, 5, 8, 8, 4, 4, 6, 6, 10, 2, 6, 3, 4, 2, 0, 8, 5, 12, 6, 6, 6, 9, 3, 4, 10, 5, 5, 3, 10, 2, 3, 6, 2, 7, 8, 8, 4, 8, 2, 5, 8, 8, 2, 4, 6, 4, 3, 4, 3, 5, 6, 8, 2, 2, 3, 5, 5, 11, 5, 4, 9, 4]

    # Histogram zapisany do pliku mysolution/1_7_histogram.png
    plt.figure(figsize=(8, 5))
    plt.hist(degrees, bins=range(min(degrees), max(degrees) + 2), edgecolor='black', alpha=0.7)
    plt.title("Histogram stopni węzłów")
    plt.xlabel("Stopień")
    plt.ylabel("Liczba węzłów")
    plt.savefig("mysolution/1_7_histogram.png")
    print("Histogram zapisano jako mysolution/1_7_histogram.png")

    # 8. Ile jest klastrów (connected components) w grafie?
    components = g.components()
    print(f"\n[8] Liczba klastrów (spójnych składowych): {len(components)}") # Odpowiedź: 2

    # 9. Zwizualizuj graf (rozmiar węzłów zależny od PageRank)
    pagerank_values = g.pagerank(weights='weight')

    # Przeskalowano PageRank razy 500 dla każdego wieżchołaka, żeby były lepiej widoczne
    vertex_sizes = [v * 500 for v in pagerank_values]

    print("\n[9] Generowanie wizualizacji...")
    layout = g.layout("fr")
    
    visual_style = {
        "vertex_size": vertex_sizes,
        "vertex_color": "darkgreen",
        "edge_width": 0.5,
        "layout": layout,
        "bbox": (800, 800),
        "margin": 50
    }
    
    # Wizualizacja zapisana w pliku: 
    ig.plot(g, "mysolution/1_9_graph_visualization.png", **visual_style)
    print("Wizualizację zapisano jako mysolution/1_9_graph_visualization.png")

if __name__ == "__main__":
    main()