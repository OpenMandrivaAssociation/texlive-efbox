Name:		texlive-efbox
Version:	33236
Release:	2
Summary:	Extension of \fbox, with controllable frames and colours
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/efbox
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/efbox.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/efbox.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/efbox.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package defines the \efbox command, which creates a box
just wide enough to hold the text created by its argument. The
command optionally puts a (possibly partial) frame around the
box, and allows setting the box background colour.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/efbox/efbox.sty
%doc %{_texmfdistdir}/doc/latex/efbox/README
%doc %{_texmfdistdir}/doc/latex/efbox/efbox.pdf
#- source
%doc %{_texmfdistdir}/source/latex/efbox/efbox.dtx
%doc %{_texmfdistdir}/source/latex/efbox/efbox.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
