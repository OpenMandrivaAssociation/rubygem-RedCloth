%define	oname	RedCloth

Summary:	A textile parser for Ruby
Name:		rubygem-%{oname}
Version:	4.2.2
Release:	3
License:	MIT
Group:		Development/Ruby
URL:		https://%{oname}.rubyforge.org/
Source0:	http://gems.rubyforge.org/gems/%{oname}-%{version}.gem
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	ruby-devel ruby-RubyGems
Requires:	ruby rubygem-ruby-hmac

%description
RedCloth is a Ruby library for converting Textile into HTML.

%prep

%build

%install
rm -rf %{buildroot}
gem install --local --install-dir %{buildroot}/%{ruby_gemdir} --force %{SOURCE0}

rm -rf %{buildroot}%{ruby_gemdir}/{cache,gems/%{oname}-%{version}/ext}
mv %{buildroot}%{ruby_gemdir}/bin %{buildroot}%{_prefix}


%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%{ruby_gemdir}/gems/%{oname}-%{version}
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec
%{_bindir}/redcloth



%changelog
* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 4.2.2-2mdv2011.0
+ Revision: 614770
- the mass rebuild of 2010.1 packages

* Thu Feb 04 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 4.2.2-1mdv2010.1
+ Revision: 500871
- import rubygem-RedCloth


* Mon Feb  4 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 4.2.2-1
- initial release
