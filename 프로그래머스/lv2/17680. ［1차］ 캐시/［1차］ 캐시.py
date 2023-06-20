def solution(cacheSize, cities):
    cache = []
    time = 0
    for city in cities :
        city = city.lower()
        if city in cache :
            time += 1
            cache.pop(cache.index(city))
            cache.append(city)
        else :
            time += 5
            if cacheSize == 0 :
                pass
            elif len(cache) < cacheSize:
                cache.append(city)
            else :
                cache.pop(0)
                cache.append(city)
    return time