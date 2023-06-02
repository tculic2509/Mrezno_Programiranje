import dns.resolver


def dns_lookup(query, record_type):
    try:
        # Izvršite DNS upit za određeni tip zapisa
        answers = dns.resolver.resolve(query, record_type)

        # Prikupite rezultate upita
        results = []
        for answer in answers:
            results.append(str(answer))

        return results

    except dns.resolver.NXDOMAIN:
        return "Nema rezultata. DNS unos ne postoji."

    except dns.resolver.NoAnswer:
        return "Nema rezultata. DNS server ne vraća odgovor."

    except dns.exception.Timeout:
        return "Nema rezultata. DNS upit je istekao."


# Unesite DNS ime ili IP adresu
query = input("Unesite DNS ime ili IP adresu: ")

# Unesite tip DNS zapisa (A, MX ili PTR)
record_type = input("Unesite tip DNS zapisa (A, MX ili PTR): ")

# Izvršite DNS upit i dohvatite rezultate
results = dns_lookup(query, record_type)

# Ispis rezultata
print("Rezultati DNS upita:")
for result in results:
    print(result)
