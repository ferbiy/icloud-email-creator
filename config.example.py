GENERATE_URL = "https://p144-maildomainws.icloud.com/v1/hme/generate"
RESERVE_URL = "https://p144-maildomainws.icloud.com/v1/hme/reserve"

QUERY_PARAMS = {
    "clientBuildNumber": "2426Hotfix10",
    "clientMasteringNumber": "2426Hotfix10",
    "clientId": "4f2affed-b51f-413a-ab0a-034399759e44",
    "dsid": "20284126077"
}

HEADERS = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6,he;q=0.5",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "text/plain",
    "Host": "p144-maildomainws.icloud.com",
    "Origin": "https://www.icloud.com",
    "Pragma": "no-cache",
    "Referer": "https://www.icloud.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"macOS"'
}

COOKIES = {
    "X_APPLE_WEB_KB-SHY8BYSMPV_S9P4AHA_EZLRTQOC": "v=1:t=AQ==BST_IAAAAAAABLwIAAAAAGdXgfkRDmdzLmljbG91ZC5hdXRovQBYBE6ZZYrwkifQj0VcCTDqwuGGa8LP6PjMBGsTvxIZseJRz2WrdK04xWT_tANeC5cjGPDdDdMySV7Nx9dB_2y9m8UooD5tLmXJxXgNUzWeJ2JNDgisd3YPqnhGobvqlq3d1QqdIZnjDmy8QPLjbJ2gtR6VYA~~",
    "X-APPLE-WEBAUTH-HSA-TRUST": "f84e2baba8314cdfa25da6fa0da6fae3254af81c3493c6f8180cccc0515bb394_HSARMTKNSRVXWFlaE8zSMskJ/GajT+hW/HGWsIeCLxwLHU/oWhhF/JzS8DAkFQzLxmKtWBrEciRWr94VZhBu10IxkAeTxKf0KEAv37M3gSNDciIDosTYhUeWVliTZELj1MoDjwQ3dfJkaoeHmpVjK5lOABP40Vsepbp1Psr3UEyzKKJXLB+qS9I1/K2Y0aFB/rbQXKxbXsmBGe/GZ+CMb8oSU+HdrE3sFx40bD8=SRVX",
    "X-APPLE-WEBAUTH-PCS-Documents": "TGlzdEFwcGw6MTpBcHBsOjE6AaYwiwTFsNdmKCUMudO97fzB+oJNBPfMStOLWNAAwxFr9uOD0+U0P0BpCXbSL99l3jnchRQHM7pFs9dzIQD+lgYgxVyrLZue2SQ8+BzzKsaDhs5GVG0voU8FhdVwYnysFWOxqlT3bcgmn9QeCR2HMBHCUmHKzWmnB6AUATDSwLgaKPq0tCS8Ag==",
    "X-APPLE-WEBAUTH-PCS-Photos": "TGlzdEFwcGw6MTpBcHBsOjE6ATHMLKrOSBPhFdY4BPOBQnOPKPeIHDH8U7bJ2sJ7HvPExdrqqrVl4h1CsCEkVhK3DBMx8s0YBAZ6G7gQeB8uh8bbBV4xwxv54TO6lf+DethHkAcT3uZ4XqS/xl/5Y/T5APqfagvjuXuDBpmksHUn/L4EkF1nk5ziUg7xeoQYBvhkVWO25BfB5w==",
    "X-APPLE-WEBAUTH-PCS-Cloudkit": "TGlzdEFwcGw6MTpBcHBsOjE6ARJl3u1Mr/56krvoaK0zeb6UHLHB4bIVWUtbv4+V6ZnHtORUUHI4e1KCWPbHuqKwCu9HtdeA5QRHrqxTn4B72nenSy03ggwIFaR3hZHWvXaTiwbHK183ekKwHegheBsyr14g7fcAo9wA08fAAFOi3UQ2osnsznVZ7dO79llUA/fNy/+zw+YoQw==",
    "X-APPLE-WEBAUTH-PCS-Safari": "TGlzdEFwcGw6MTpBcHBsOjE6AXjkTdIrsccv2EQenUzrOdIlqo5rZQapAQYm43KmqsoyX7fp0N6bnX/4seGe8GR/iK2sLTnrzvTqZdkN9JKYoeOQpTtZvL4cupJG3UMJoXMpWlKBF2pSyvz/VFWP5Vx7SR0/g+rexHpGKGOrA2PKHFSO4D4vQWVpNqSH7BZcappj2o0IwulRLA==",
    "X-APPLE-WEBAUTH-PCS-Mail": "TGlzdEFwcGw6MTpBcHBsOjE6ASTFCGPIMvMusl7DvX6GyoL+6aEGlC5+fADNUgw87vP01FWZLfW8f3UXNb5hE9nLpTOulDRbfagt7UxwTSJ4ly2/Bqixhx7E/HPop1jeZjYsF2Ubn6nBzpajlIOSuQxROAMi2rQCeNgk3fO6hwFzdfUYRwqtUdxLKXD1XyCRRCw/hijWAKgGdQ==",
    "X-APPLE-WEBAUTH-PCS-Notes": "TGlzdEFwcGw6MTpBcHBsOjE6Aa2sfbyL4EWDCsakzD0/N2sCIumxPBPm4eFOj+Qdt2ikBCK5RDb3302b8KqUlDhPAw2N2aJf9MZmaWFpQi/cGFz4IoJKFeKVSGEYVIAewpUwNSaaGECSu8sEJNnu4PUayj985wzz7cAPlMZzXbtPdqYku4wS1wRSxJbJMpUYo3TEXRt3gLrXQw==",
    "X-APPLE-WEBAUTH-PCS-News": "TGlzdEFwcGw6MTpBcHBsOjE6AeWQrIYYmKCgxit2dFG7lsXxDPJLOz1wHXgVA59Jh/si5JwLdMOVZyRcUtHUnxDk7KvXoZQdkf6QXy1X/4ntU0UlOAdzSlk3mHjLcG2rmtihaDXthLXt1wPbWJA5xbEFY/qk0ULboUPMvZiDO85UykIjc+IdAi39S6sW42K8uLyNcJnTkTrWQg==",
    "X-APPLE-WEBAUTH-PCS-Sharing": "TGlzdEFwcGw6MTpBcHBsOjE6AUfqzkD2geEvX5Y9Fs5li6pUKciZy/OAuNeVjJNDcFdAA7/tub405QhkDCicFOrKYr96dl5Aba90Iowa75jbXhUazN1jEN+dPpbTz4ZK1a8jtjjiochpwPfMbN3RQhTmi+8FhE+2jvNjW1amFYNrv+x4iVkqR4fSPhqVaFvFfuZZUJ9Z+1p57w==",
    "X-APPLE-WEBAUTH-USER": "v=1:s=1:d=20284126077",
    "X-APPLE-DS-WEB-SESSION-TOKEN": "AQFGH/Zv6mw2pKCww9uYq+xYQieLjSMhNm717I+n0LVUJT34B5h3360YTT21TSUaBww74idj2MoKMjlPTu9Z5TDAIvl5t2ZVfFL6rqELZxOYKZQ/NGtus+fL/oqck4wGtK8PHOIYfyXr1pM/1xr557aLnFU6NAxmffU70NJg6cDF0J90mUUuLOhL3OjV6m71Pz+AeAEAXZRkrVQKB/e6q2wrEaDxc7cNzkESdht8SNgyv09mNV5Sl/Iwc5tHit03Wg18lYvUvTBdLktDU4uNNwMOhilR0ULchIBI8BTHyVNzoHC7je6BcRtwm6hZBmQFtfWVnHZbCzr/Hsi65RRoSSF4a3tA9TxH7uttAcvHChotH7zfHcE0bfgxHXvp1cnfB6L5lK6NpKehd+KEf71sPLHQHlnNsuDzz4/mxbiil1obeVkDK9ydQjnPHSDQY/zk3imhGpxEaJS6Ds7p+gqlrCTkPNfe47+GQc8jn1aGb1mFGu1uxtbn5Vus6SzmN2FnLX7g5HaEIjHNsqsv7oVdYX9n4/w+XAu8Cf5t5B1Gil1R+NyzlJVpWloZgVKtxFYatomtGt5HEn19aPHNBmTKd43zorMzJflG90GEeHtqPAhdQmJAl0b3MhoOxa9Vv4h7/RzFFUZIYd+s4/8VFpmcxtH183OBORp1KecL/hMB/9UVLGdqMQrt1zAk+RVSOuU0RAwRD10S9PLIUV337LgegKnMyH/D0f0wZAIvkKJacd/c1hhhW5womtwq3ZI3qcQfDGit1K518pRVwcTifXJp80NdHauR+rPKq2Ktmw==",
    "X-APPLE-WEB-ID": "A9252B650E0583FF846C502F483772064CED5E9A",
    "X-APPLE-WEBAUTH-VALIDATE": "v=1:t=Aw==BST_IAAAAAAABLwIAAAAAGdhYeQRDmdzLmljbG91ZC5hdXRovQCjID9ImWmbGqTNHNHI1n9BJSLzc1f3RyE3umVotl7R9Y2_r2puXlH7woTWBKtrQYo6BOhKFySzuzJlNATVgj2YsgRss9K_DNrf2tDxw_sr0VtlqvIqbUJO0Zre1KHxxl2PP1WTUKlXJboffGG4z0sbRyeUSw~~",
    "X-APPLE-WEBAUTH-TOKEN": "v=2:t=Aw==BST_IAAAAAAABLwIAAAAAGdhYiQRDmdzLmljbG91ZC5hdXRovQADktXsLrEBCJNUkOaMMLLWlN_wXQzXQMfDeWvBwDOVY2ILNqgoS-6YeTFh04fRZw_Gwb-Bz1gq3DTLglED6l4Jw0J0tlDBQfvmqg_A4qpTkpun_YBqVcalg11x7KtFKIjd40V6qsfFetoRYAJ27-GMyF9XJA~~"
} 