def dif(s1, s2, n):
    dif = 0
    for i in range(n):
        if s1[i] != s2[i]:
            dif += 1
    return dif

# @param start, a string
# @param end, a string
# @param dict, a set of string
# @return an integer
def ladderLength(start, end, dict):
    n = len(start)
    s_start = set()
    s_end = set()
    for d in dict:
        if dif(d, start, n) == 1:
            s_start.add(d)
    for d in dict:
        if dif(d, end, n) == 1:
            s_end.add(d)
    if not len(s_start) or not len(s_end):
        return 0
    if start in s_end or end in s_start:
        return 1

    s_start_now = s_start
    s_start_next = set()
    s_start_used = set()
    s_end_now = s_end
    s_end_next = set()
    s_end_used = set()
    for i in range(n/2):
        for t1 in s_start_now:
            for d in dict:
                if dif(d, t1, n) == 1 and not d in s_start_used:
                    s_start_next.add(d)
                    s_start_used.add(d)
        for e in s_end_now:
            if e in s_start_next:
                return 2*i + 4
        for t1 in s_end_now:
            for d in dict:
                if dif(d, t1, n) == 1 and not d in s_end_used:
                    s_end_next.add(d)
                    s_end_used.add(d)
        for s in s_start_next:
            if s in s_end_next:
                return 2*i + 5
        s_start_now = s_start_next
        s_start_next = set()
        s_end_now = s_end_next
        s_end_next = set()
    return 0
start = "nape"
end = "mild"
dd = {"dose","ends","dine","jars","prow","soap","guns","hops","cray","hove","ella","hour","lens","jive","wiry","earl","mara","part","flue","putt","rory","bull","york","ruts","lily","vamp","bask","peer","boat","dens","lyre","jets","wide","rile","boos","down","path","onyx","mows","toke","soto","dork","nape","mans","loin","jots","male","sits","minn","sale","pets","hugo","woke","suds","rugs","vole","warp","mite","pews","lips","pals","nigh","sulk","vice","clod","iowa","gibe","shad","carl","huns","coot","sera","mils","rose","orly","ford","void","time","eloy","risk","veep","reps","dolt","hens","tray","melt","rung","rich","saga","lust","yews","rode","many","cods","rape","last","tile","nosy","take","nope","toni","bank","jock","jody","diss","nips","bake","lima","wore","kins","cult","hart","wuss","tale","sing","lake","bogy","wigs","kari","magi","bass","pent","tost","fops","bags","duns","will","tart","drug","gale","mold","disk","spay","hows","naps","puss","gina","kara","zorn","boll","cams","boas","rave","sets","lego","hays","judy","chap","live","bahs","ohio","nibs","cuts","pups","data","kate","rump","hews","mary","stow","fang","bolt","rues","mesh","mice","rise","rant","dune","jell","laws","jove","bode","sung","nils","vila","mode","hued","cell","fies","swat","wags","nate","wist","honk","goth","told","oise","wail","tels","sore","hunk","mate","luke","tore","bond","bast","vows","ripe","fond","benz","firs","zeds","wary","baas","wins","pair","tags","cost","woes","buns","lend","bops","code","eddy","siva","oops","toed","bale","hutu","jolt","rife","darn","tape","bold","cope","cake","wisp","vats","wave","hems","bill","cord","pert","type","kroc","ucla","albs","yoko","silt","pock","drub","puny","fads","mull","pray","mole","talc","east","slay","jamb","mill","dung","jack","lynx","nome","leos","lade","sana","tike","cali","toge","pled","mile","mass","leon","sloe","lube","kans","cory","burs","race","toss","mild","tops","maze","city","sadr","bays","poet","volt","laze","gold","zuni","shea","gags","fist","ping","pope","cora","yaks","cosy","foci","plan","colo","hume","yowl","craw","pied","toga","lobs","love","lode","duds","bled","juts","gabs","fink","rock","pant","wipe","pele","suez","nina","ring","okra","warm","lyle","gape","bead","lead","jane","oink","ware","zibo","inns","mope","hang","made","fobs","gamy","fort","peak","gill","dino","dina","tier"}

print ladderLength(start, end, dd)