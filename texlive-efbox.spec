# revision 33236
# category Package
# catalog-ctan /macros/latex/contrib/efbox
# catalog-date 2014-03-28 17:26:17 +0100
# catalog-license lppl1.3
# catalog-version 1.0
Name:		texlive-efbox
Version:	1.0
Release:	4
Summary:	Extension of \fbox, with controllable frames and colours
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/efbox
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/efbox.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/efbox.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/efbox.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
