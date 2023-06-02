import dns.resolver

def dns_lookup(query, record_type):
    try:
        answers = dns.resolver.resolve(query, record_type)
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
query = input("Unesite DNS ime ili IP adresu: ")

record_type = input("Unesite tip DNS zapisa (A, MX ili PTR): ")

results = dns_lookup(query, record_type)
print("Rezultati DNS upita:")
for result in results:
    print(result)
