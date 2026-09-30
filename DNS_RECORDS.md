# kettlongear.com DNS at Squarespace (GitHub Pages)

Delete the "Squarespace Defaults" preset first (the four A records and the www CNAME), then add these five custom records.

| Type | Host | Data | TTL |
| --- | --- | --- | --- |
| A | @ | 185.199.108.153 | 1 hr |
| A | @ | 185.199.109.153 | 1 hr |
| A | @ | 185.199.110.153 | 1 hr |
| A | @ | 185.199.111.153 | 1 hr |
| CNAME | www | keneliteedganalytics.github.io | 1 hr |

Leave the Email Security TXT records and the Domain Connect CNAME alone.
GitHub side is already set: repository keneliteedganalytics/kettlongear, Pages on main, custom domain kettlongear.com, HTTPS enforcement turns on automatically once DNS resolves (usually within an hour).
