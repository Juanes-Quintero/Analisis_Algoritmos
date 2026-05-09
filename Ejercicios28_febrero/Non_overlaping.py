class Solution:
    def eraseOverlapIntervals(self, intervalos: list[list[int]]) -> int:
        """
        Estrategia Greedy:
        Ordenar los intervalos por su tiempo de finalización.

        Idea:
        Mantener siempre el intervalo que termine primero
        para evitar más solapamientos futuros.

        Complejidad:
        Tiempo: O(n log n)
        Espacio: O(1)
        """

        # ordenar por tiempo de finalización
        intervalos.sort(key=lambda intervalo: intervalo[1])

        eliminados = 0

        # tomar el final del primer intervalo
        fin_anterior = intervalos[0][1]

        for i in range(1, len(intervalos)):

            inicio_actual = intervalos[i][0]
            fin_actual = intervalos[i][1]

            # hay solapamiento
            if inicio_actual < fin_anterior:
                eliminados += 1
            else:
                # actualizar último intervalo válido
                fin_anterior = fin_actual

        return eliminados