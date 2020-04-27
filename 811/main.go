package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {
	fmt.Println(subdomainVisits([]string{"900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"}))
}

func subdomainVisits(cpdomains []string) []string {
	totalVisits := map[string]int{}
	for _, visit := range cpdomains {
		values := strings.Split(visit, " ")
		visits, _ := strconv.Atoi(values[0])
		domain := values[1]
		for strings.IndexByte(domain, '.') != -1 {
			if _, ok := totalVisits[domain]; !ok {
				totalVisits[domain] = visits
			} else {
				totalVisits[domain] += visits
			}
			domain = domain[strings.IndexByte(domain, '.')+1:]
		}
		if _, ok := totalVisits[domain]; !ok {
			totalVisits[domain] = visits
		} else {
			totalVisits[domain] += visits
		}
	}
	results := []string{}
	for k, v := range totalVisits {
		results = append(results, fmt.Sprintf("%d %s", v, k))
	}
	return results
}
