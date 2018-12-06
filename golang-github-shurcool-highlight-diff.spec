# Run tests in check section
%bcond_without check

%global goipath         github.com/shurcooL/highlight_diff
%global commit          09bb4053de1b1d872a9f25dc21378fa71dca4e4e

%global common_description %{expand:
highlight_diff provides syntaxhighlight.Printer and syntaxhighlight.Annotator 
implementations for diff format. It implements intra-block character-level 
inner diff highlighting.}

%gometa

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        Syntax highlighter for diff format
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires: golang(github.com/sergi/go-diff/diffmatchpatch)
BuildRequires: golang(github.com/sourcegraph/annotate)
BuildRequires: golang(github.com/sourcegraph/syntaxhighlight)

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%doc README.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git09bb405
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 24 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20180418git09bb405
- First package for Fedora

