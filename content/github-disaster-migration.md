Title: Github disaster migration
Date: 2016-01-16 14:33:00
Modified: 2016-01-16 14:33:00
Slug: github-disaster-migration
Authors: George Nikolopoulos
Summary: How do you get out of github?

I read recently the [dear github][1], document
which presents some issues developers have with github and hints that the solution
to these problems could be the open sourcing of the platform since said developers could
then submit patches to address the issues they have. It is also signed by quite a few developers
that are using github, and should I had used github more frequently I would sign too.

This reminded me of another criticism of github that I have been thinking of lately.
_How diffcult or easy is a migration from github?_

The scenario I think of is the following. You have been developing a project on github.
Probably you have a few contributors that use all the facilities of github to collaborate.
Pull requests, issue tracking, wiki hosting, git hosting etc.

One fine day you wake up and you cannot login to github, it is a "server not found" message.
You say to yourself, no way. Github messed up with their DNS resolution? No no it's my fault
somehow, I shouldn't have mocked around with dnsmasq last night. Just to be sure you check
with your favorite search engine the web for "github outage" and voilà!
You see the most absurd news posts. Aliens landed on earth last night with large planet destroyers
in orbit ready to annihilate the human civilization. But, they decided to have a laugh first.
They started wiping out _every_ digital imprint of famous web sites and internet services.
Being superior technologically they scanned all of the internet in 10ms and started from the shell
of the net to the core. First target was github. It went out in 1ms.
All digital imprint of github was deleted.  No trace remains. Just as if it had never existed.
Now being a stereotypical, ego centric nerd you go into a rage: "What? They wiped out _my project?_".
"How can I recover the project's work and those of the fellow contributors from what I have on my own computer?"
not noticing the fact that the entire planet is going to kick the bucket in a matter of hours.

Aside from the comic relief, this question is a valid one and one that I have actually considered. A more real world
example could be thought of, like a take down of a project as the result of legal proceedings, which
if memory serves it has actually happened in the past.

More than that, can we replicate the work in github relying only on open source technologies
and public protocols?

I have not researched the technical side of it. I am sure there are technical solutions that work
to some extent.  Just off the top of my head my guess is that a github project could be replicated using HTTP served by nginx ,
mailing lists hosted on mailman for issues and pull requests replication and  static site generators like pelican
for wiki content and git for the repository.

The deeper, philosophical question if you please, is: Can we replicate, even in
archival form, the sum of the information github hosts for a given project? Is it possible to
write a script that scrapes your project daily and updates an off site replica? Should the disaster
happen could you point to an ip address or a domain name and be able to say to your users: "Don't worry guys and girls.
All work up until last night has been saved on http://my-project.com" .
Is the walled garden impossible to cross without leaving something behind? The ever changing technical landscape
formed by the open source community as whole that addresses these issues is, I believe, the best way
to add to the credibility and weight the [dear github][1] complain carries.

Finally I can't help but notice the deep irony of using github to complain about github services.

And yes, I am aware that the same irony applies to this blog post being hosted on github. ;)

[1]: https://github.com/dear-github/dear-github
