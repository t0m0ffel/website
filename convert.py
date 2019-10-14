with open('config.toml') as config, open('out.txt', 'w') as out:
    import re


    def s(st):
        return ' '.join(st.split())


    text = s(config.read().replace("\n", " "))

    out.writelines([line + "\n\n" for line in re.findall('"""(.*?)"""', text)])
