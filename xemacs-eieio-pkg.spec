Summary:	framework for writing object oriented applications in emacs lisp
Name:		xemacs-eieio-pkg
%define 	srcname	eieio
Version:	1.04
Release:	1
License:	GPL
Group:		Applications/Editors/Emacs
Source0:	ftp://ftp.xemacs.org/xemacs/packages/%{srcname}-%{version}-pkg.tar.gz
URL:		http://www.xemacs.org/
BuildArch:	noarch
Requires:	xemacs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
EIEIO is a framework for writing object oriented applications in emacs
lisp, and is a result of my taking various object oriented classes at
work and my attempt to understand some of it better by implementing it.
The real reason I started eieio is because someone in one of my classes
said "I bet emacs can't do that!".  Well then, I just had to prove them
wrong!

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

cp -a * $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

# remove .el file if corresponding .elc file exists
find $RPM_BUILD_ROOT -type f -name "*.el" | while read i; do test ! -f ${i}c || rm -f $i; done

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# %doc lisp/eieio/ChangeLog
# %{_datadir}/xemacs-packages%{_sysconfdir}/*
%dir %{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages/lisp/*/*
%{_datadir}/xemacs-packages/pkginfo/*
%{_datadir}/xemacs-packages/info/*