%global tl_name efbox
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Extension of \fbox, with controllable frames and colours
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/efbox
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/efbox.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/efbox.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/efbox.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package defines the \efbox command, which creates a box just wide
enough to hold the text created by its argument. The command optionally
puts a (possibly partial) frame around the box, and allows setting the
box background colour.

