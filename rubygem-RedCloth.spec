%define	oname	RedCloth

Summary:	A textile parser for Ruby
Name:		rubygem-%{oname}
Version:	4.2.2
Release:	%mkrel 1
License:	MIT
Group:		Development/Ruby
URL:		http://%{oname}.rubyforge.org/
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

