# View my résumé in your Terminal!

Its my résumé, but in the terminal.

With just `curl` in your terminal, you can navigate my website, which primarily hosts my résumé.

## Examples

### Linux, MacOS

``` bash
# home page
curl -s m6freeman.sh

# my full résumé
curl -s m6freeman.sh | less -r
```

- `curl`'s `-s` just means `--silent`. `curl`'s progress bar can leave unsightly artifacts, so this is recommended
- Piping the `/resume` page into `less` or the pager of your choice is recommended in order to start at the top. `less`'s `-r` renders the ANSI characters

### Windows

#### CMD (recommended)

``` cmd

curl -s m6freeman.sh
```

#### Powershell (not recommended)

``` powershell

Invoke-WebRequest -Uri "m6freeman.sh" | Select-Object Content
```

![welcome page](./img.png)

## Shout Outs

 - Heavily inspired by [YSAP](https://www.youtube.com/watch?v=ddG_thnxt9A)'s website `ysap.sh`. I thought this was such a clever idea and figured I could do that but within my own tech stack.

